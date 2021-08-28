racket1 = Player("racket.png", 30, 200, 4, 50, 150)
racket2 = Player("racket.png", 520, 200, 4, 50, 150)
ball = GameSprite("tennis_ball", 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render("PLAYER 1 LOSE!"), True, (180, 0, 0)
lose2 = font.render("PLAYER 2 LOSE!"), True, (180, 0, 0)

speed_x = 3
speed_y = 3
