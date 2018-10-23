class Disc:
    def __init__(self,w,h,x,y):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        global select
    def draw(self):
        # print(select,t)
        # print(self.x)
        if select and self.x/100 == (2*t)+1:
            fill(255,0,0)
        else:
            fill(255,255,255)
        rectMode(CENTER)
        stroke(0,0,0)
        strokeWeight(1)
        rect(self.x,self.y,self.w,self.h)

class Tower:  
    def __init__(self,x):
        self.discs = []
        self.x = x
    def push(self,d):
        self.discs.append(d)
    def pop(self):
        return self.discs.pop()
    def top(self):
        return self.discs[-1]
    def startTower(self):
        w = 120
        y = 175
        h = 12
        while w > 0:
            d = Disc(w,h,self.x,y)
            self.discs.append(d)
            w -= 12
            y -= 12
    def draw(self):
        stroke(125,125,125)
        strokeWeight(5)
        line(self.x,25,self.x,175)
        line(self.x,25,self.x,175)
        line(self.x,25,self.x,175)
        for item in self.discs:
            item.draw()

class Board:
    def __init__(self):
        global select
        self.towers = []
        tower0 = Tower(100)
        self.towers.append(tower0)
        tower1 = Tower(300)
        self.towers.append(tower1)
        tower2 = Tower(500)
        self.towers.append(tower2)
    def startBoard(self):
        self.towers[0].startTower()
        select = False
    def updateBoard(self):
        global t
        global t2
        if t != -1:
            if len(self.towers[t].discs) > 0: #if discs in source tower
                disc = self.towers[t].top()
                if t2 != -1: #if able to select destination
                    if len(self.towers[t2].discs) == 0: #if no discs in new tower
                        # print(t,t2)
                        # print(self.towers[t].discs[-1].w)
                        self.towers[t].top().x = self.towers[t2].x
                        self.towers[t].top().y = 175-12*len(self.towers[t2].discs)
                        self.towers[t2].push(self.towers[t].pop())
                        t = -1
                        t2 = -1
                    elif len(self.towers[t2].discs) > 0:
                        disc2 = self.towers[t2].top()
                        if disc2.w > disc.w:
                            self.towers[t].top().x = self.towers[t2].x
                            self.towers[t].top().y = 175-12*len(self.towers[t2].discs)
                            self.towers[t2].push(self.towers[t].pop())
                            t = -1
                            t2 = -1
                        else:
                            t = -1
        redraw()
    def draw(self):
        # fill(0,0,0)
        # stroke(0,0,0)
        for item in self.towers:
            item.draw()
        
def setup():
    size(600,200)
    background(200,200,200)
    global board
    board = Board()
    board.startBoard()
    global mouseX
    global mouseY
    global t
    t = -1
    global t2
    t2 = -1
    global select
    select = False
    
def mouseClicked():
    global mouseX
    global mouseY
    global t
    global t2
    global select
    if not select:
        if mouseX > 50 and mouseX < 150:
            t = 0
        elif mouseX > 250 and mouseX < 350:
            t = 1
        elif mouseX > 450 and mouseX < 550:
            t = 2
        else:
            t = -1
    else:
        if mouseX > 50 and mouseX < 150:
            t2 = 0
        elif mouseX > 250 and mouseX < 350:
            t2 = 1
        elif mouseX > 450 and mouseX < 550:
            t2 = 2
        else:
            t2 = -1
    select = not select
    redraw();
    
def draw():
    global board
    background(255,255,255)
    board.draw()
    board.updateBoard()