import time
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication,QMessageBox,QMainWindow
from PySide2.QtGui import QIcon,QPixmap,QPalette,QBrush
import pygame as pg
from machine import people_machine
class UI_interface:#ui界面和游戏界面
    def __init__(self):
        self.ui = QUiLoader().load(r"1.8ui.ui")#加载ui
        self.window=QMainWindow()
        self.ui.setWindowTitle('五子棋')
        self.button=QPushButton()
        palette = QPalette()
        palette.setBrush(QPalette.Window,QBrush(QPixmap(r'C:\Users\Kyle Zhou\Desktop\课程设计项目\bg.jpg')))#加载第一界面背景
        self.ui.setPalette(palette)
        url = QUrl.fromLocalFile(r"C:\Users\Kyle Zhou\Downloads\13286.wav")#导入古筝音乐
        content = QMediaContent(url)
        self.player = QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()#播放第一界面音乐
        self.ui.pushButton.setStyleSheet("background-image: url(button_picture.jpg);")
        self.ui.pushButton_2.setStyleSheet("background-image: url(button_picture.jpg);")
        self.ui.pushButton_3.setStyleSheet("background-image: url(button_picture.jpg);")
        self.ui.pushButton_4.setStyleSheet("background-image: url(button_picture.jpg);")
        self.ui.pushButton_5.setStyleSheet("background-image: url(button_picture.jpg);")
        self.ui.pushButton.clicked.connect(self.play_game)
        self.ui.pushButton_2.clicked.connect(self.quit)
        self.ui.pushButton_3.clicked.connect(self.introduction)
        self.ui.pushButton_4.clicked.connect(self.person)
    def play_game(self):#游戏开始按钮函数
        box = QMessageBox()#弹出游戏模式选择按钮
        box.setWindowTitle('游戏模式')
        box.setIconPixmap(QPixmap(r"C:\Users\Kyle Zhou\Downloads\运行.png").scaled(100, 100))
        box.setText('<h3>请选择游戏模式</h3>')
        reply=box.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        buttonY = box.button(QMessageBox.Yes)
        buttonY.setStyleSheet("QPushButton:hover {color: black ;font-size:30px;}")
        buttonY.setText('双人模式')
        buttonN = box.button(QMessageBox.No)
        buttonN.setStyleSheet("QPushButton:hover {color: black ;font-size:30px;}")
        buttonN.setText('人机模式')
        box.exec_()#等待用户选择
        if box.clickedButton()==buttonY:
            self.people_by_people()#用户选择双人模式，则进入people_by_people方法
        else:
            people_machine()
    def introduction(self):#游戏简介按钮
        # self.player.stop()#让古筝音乐停止
        box = QMessageBox()
        box.setText('五子棋是全国智力运动会竞技项目之一，是一种两人对弈的纯策略型棋类游戏。五子棋的棋具与围棋通用，是一种传统的棋种，有两种玩法。'
                    '一种是双方分别使用黑白两色的棋子，下在棋盘直线与横线的交叉点上，先形成五子连线者获胜。还有一种是自己形成五子连线就替换对方任意一枚棋子。'
                    '被替换的棋子可以和对方交换棋子。最后以先出完所有棋子的一方为胜。五子棋容易上手，老少皆宜，而且趣味横生，引人入胜：'
                    '它不仅能增强思维能力，提高智力，而且富含哲理，有助于修身养性。')
        box.setIconPixmap(QPixmap(r"C:\Users\Kyle Zhou\Downloads\游戏简介图标-01.png").scaled(90,90))
        box.setWindowTitle('游戏简介')
        box.setStandardButtons(QMessageBox.Yes)
        box.button(QMessageBox.Yes).setText('好的')
        box.button(QMessageBox.Yes).setStyleSheet("QPushButton:hover {color: black ;font-size:30px;}")
        box.exec_()#等待用户选择按钮

    def person(self):#制作人员按钮
        box = QMessageBox()
        box.setWindowTitle('制作人员')
        box.setText('kyle_zhou')
        box.setIconPixmap(QPixmap(r"C:\Users\Kyle Zhou\Downloads\关于我们.png").scaled(100, 100))
        box.setStandardButtons(QMessageBox.Yes)
        box.button(QMessageBox.Yes).setText('好的')
        box.button(QMessageBox.Yes).setStyleSheet("QPushButton:hover {color: black ;font-size:30px;}")
        box.exec_()#等待用户选择按钮

    def quit(self):#退出游戏按钮
        box = QMessageBox()
        box.setWindowTitle('警告!')
        box.setIconPixmap(QPixmap(r"C:\Users\Kyle Zhou\Downloads\警告.png").scaled(70, 70))
        box.setText('<h3>确认退出游戏？</h3>')
        reply = box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = box.button(QMessageBox.Yes)
        buttonY.setStyleSheet("QPushButton:hover {color: black ;font-size:30px;}")
        buttonY.setText('确认')
        buttonN = box.button(QMessageBox.No)
        buttonN.setStyleSheet("QPushButton:hover {color: black ;font-size:30px;}")
        buttonN.setText('取消')
        box.exec_()
        if box.clickedButton()==buttonY:
            app.quit()#如果用户按确认键，则退出整个应用
        else:
            pass#否则，只退出Qmessagebox

    def people_by_people(self):
        class Chessboard:  # 设置棋盘
            def __init__(s):
                s.grid_lenght = 26  # 棋盘格子的边长
                s.grid_count = 20  # 格子的数量
                s.start_x = 150  # 棋盘初始点坐标，左上角的坐标
                s.start_y = 50
                s.edge_lenght = s.grid_lenght / 2  # 棋盘周围边缘的长度13
                s.piece = "black"
                s.winner = None
                s.gameover = False
                s.grid = []
                for i in range(s.grid_count):  # 棋盘大小为20*20个格子
                    s.grid.append(list("." * s.grid_count))

            def handle_event(s, e):
                origin_x = s.start_x - s.edge_lenght
                origin_y = s.start_y - s.edge_lenght
                chessboard_lenght = (s.grid_count - 1) * s.grid_lenght + s.edge_lenght * 2
                mouse_pos = e.pos  # 鼠标位置在棋盘坐标内
                if (mouse_pos[0] > origin_x and mouse_pos[0] <= origin_x + chessboard_lenght) and (
                        mouse_pos[1] >= origin_y and mouse_pos[1] <= origin_y + chessboard_lenght):
                    if not s.gameover:
                        x = mouse_pos[0] - origin_x  # X轴方向距离
                        c = int(x / s.grid_lenght)  # 换算出X轴第几格
                        y = mouse_pos[1] - origin_y
                        r = int(y / s.grid_lenght)  # 换算出Y轴第几格
                        if s.set_piece(r, c):
                            s.check_win(r, c)

            def set_piece(s, r, c):
                if s.grid[r][c] == ".":  # 该位置没有棋子
                    s.grid[r][c] = s.piece
                    if s.piece == "black":  # 交替使用棋子
                        s.piece = "white"
                    else:
                        s.piece = "black"
                    return True
                return False

            def check_win(s, r, c):
                n_count = s.get_continuous_count(r, c, -1, 0)  # 上方向相周颜色棋子数量
                s_count = s.get_continuous_count(r, c, 1, 0)  # 下方相同颜色棋子数量
                w_count = s.get_continuous_count(r, c, 0, -1)  # 左方
                e_count = s.get_continuous_count(r, c, 0, 1)  # 右方
                nw_count = s.get_continuous_count(r, c, -1, -1)  # 左上方
                ne_count = s.get_continuous_count(r, c, -1, 1)  # 右上方
                sw_count = s.get_continuous_count(r, c, 1, -1)  # 左下方
                se_count = s.get_continuous_count(r, c, 1, 1)  # 右下方
                if (n_count + s_count + 1 >= 5) or (e_count + w_count + 1 >= 5) or (se_count + nw_count + 1 >= 5) or (
                        ne_count + sw_count + 1 >= 5):
                    s.winner = s.grid[r][c]
                    s.gameover = True

            def get_continuous_count(s, r, c, dr, dc):  # 统计一个方向的同颜色棋子数量
                piece = s.grid[r][c]
                result = 0
                i = 1
                while True:
                    new_r = r + dr * i
                    new_c = c + dc * i
                    if 0 <= new_r < s.grid_count and 0 <= new_c < s.grid_count:
                        if s.grid[new_r][new_c] == piece:  # 该方向颜色相同则加上
                            result += 1
                        else:
                            break
                    else:
                        break
                    i += 1
                return result

            def draw(s, screen):
                pg.draw.rect(screen, (185, 122, 87), [s.start_x - s.edge_lenght, s.start_y - s.edge_lenght,  # 画棋盘
                                                      (s.grid_count - 1) * s.grid_lenght + s.edge_lenght * 2,
                                                      (s.grid_count - 1) * s.grid_lenght + s.edge_lenght * 2], 0)
                for r in range(s.grid_count):  # 画棋盘横线
                    y = s.start_y + r * s.grid_lenght
                    pg.draw.line(screen, (0, 0, 0), [s.start_x, y], [s.start_x + s.grid_lenght * (s.grid_count - 1), y],
                                 2)
                for c in range(s.grid_count):  # 画棋盘竖线
                    x = s.start_x + c * s.grid_lenght
                    pg.draw.line(screen, (0, 0, 0), [x, s.start_y], [x, s.start_y + s.grid_lenght * (s.grid_count - 1)],
                                 2)
                for r in range(s.grid_count):
                    for c in range(s.grid_count):
                        piece = s.grid[r][c]
                        if piece != ".":
                            if piece == "black":  # 设置棋子颜色
                                color = (45, 45, 45)
                            else:
                                color = (219, 219, 219)
                            x = s.start_x + c * s.grid_lenght
                            y = s.start_y + r * s.grid_lenght
                            pg.draw.circle(screen, color, [x, y], s.grid_lenght // 2)  # 在棋盘上画棋子

        class Gomoku:
            def __init__(s):
                pg.init()
                s.just_one=1
                s.surface=pg.image.load(r"C:\Users\Kyle Zhou\Downloads\多人游戏2.png")
                pg.display.set_icon(s.surface)
                s.screen = pg.display.set_mode((1040, 780))
                pg.display.set_caption("五子棋对战")
                s.clock = pg.time.Clock()
                s.font = pg.font.Font(u"C:\Windows\Fonts\Candarab.ttf", 24)
                s.going = True
                s.chessboard = Chessboard()

            def updates(s):  # 更新画面
                for e in pg.event.get():
                    if e.type == pg.QUIT:
                        s.going = False
                    elif e.type == pg.MOUSEBUTTONDOWN:
                        s.chessboard.handle_event(e)

            def draw(s):
                s.screen.fill((255, 255, 255))  # 窗口底色为白色
                s.screen.blit(s.font.render("FPS:{0:.2F}".format(s.clock.get_fps()), True, (0, 0, 0)), (10, 10))
                s.chessboard.draw(s.screen)  # 画棋盘窗口
                pg.display.update()  # 更新界面

            def loop(s):#主循环
                while s.going:
                    s.updates()
                    s.draw()
                    s.clock.tick(100)
                    if s.chessboard.winner and s.just_one==1:
                        time.sleep(0.5)
                        url = QUrl.fromLocalFile(r"C:\Users\Kyle Zhou\Downloads\14230.wav")
                        content = QMediaContent(url)
                        self.player = QMediaPlayer()
                        self.player.setMedia(content)#游戏胜利音效
                        self.player.play()
                        box=QMessageBox()
                        box.setWindowTitle('游戏结束')
                        box.setIconPixmap(QPixmap(r"C:\Users\Kyle Zhou\Downloads\奖杯，胜利，赢了，完成，比赛.png").scaled(50,50))
                        if s.chessboard.winner=="white":
                            s.chessboard.winner="白棋"
                        if s.chessboard.winner=="black":
                            s.chessboard.winner="黑棋"
                        box.setText('<h3>{}获胜!!!</h3>'.format(s.chessboard.winner))
                        box.setStandardButtons(QMessageBox.Yes)
                        buttonY = box.button(QMessageBox.Yes)
                        buttonY.setText('好的')
                        buttonY.setStyleSheet("QPushButton:hover {color: black ;font-size:25px;}")
                        box.exec_()
                        s.just_one=0
                pg.quit()

        if __name__ == "__main__":
            game = Gomoku()
            game.loop()

app = QApplication([])
app.setWindowIcon(QIcon(r"C:\Users\Kyle Zhou\Downloads\小棋盘.png"))
stats = UI_interface()
stats.ui.show()
app.exec_()