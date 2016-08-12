from random import randint

def minesweep():
    for i in range(20):
        print "MINESWEEP"
    board = []
    size = int(raw_input('How big of a field do you want to play in? '))
    for i in range(size):
        board.append(["O"] * size)
    def printer(board):
        for row in board:
            print " ".join(row)
    printer(board)
    def gen_mine():
        return [randint(0, size - 1), randint(0, size - 1)]
    mine_count = 0
    mines = []
    for i in range(size * 2):
        if mine_count < int(size ** 2 / 6):
            pair = gen_mine()
            if pair not in mines:
                mines.append(pair)
                mine_count += 1
    def surrounding(pair):
        surround = []
        surround.append([pair[0] - 1, pair[1]])
        surround.append([pair[0] - 1, pair[1] - 1])
        surround.append([pair[0] - 1, pair[1] + 1])
        surround.append([pair[0], pair[1] - 1])
        surround.append([pair[0], pair[1] + 1])
        surround.append([pair[0] + 1, pair[1]])
        surround.append([pair[0] + 1, pair[1] - 1])
        surround.append([pair[0] + 1, pair[1] + 1])
        return surround
    def danger(pair):
        count = 0
        surround = surrounding(pair)
        for pair in surround:
            if pair in mines:
                count += 1
        return str(count)
    def clear(pair):
        if pair[0] == 0 and pair[1] == 0:
            board[pair[1] + 1][pair[0]] = danger([pair[0], pair[1] + 1])
            board[pair[1] + 1][pair[0] + 1] = danger([pair[0] + 1, pair[1] + 1])
            board[pair[1]][pair[0] + 1] = danger([pair[0] + 1, pair[1]])
        elif x == len(board) - 1 and y == len(board) - 1:
            board[pair[1] - 1][pair[0]] = danger([pair[0], pair[1] - 1])
            board[pair[1] - 1][pair[0] - 1] = danger([pair[0] - 1, pair[1] - 1])
            board[pair[1]][pair[0] - 1] = danger([pair[0] - 1, pair[1]])
        elif pair[0] == 0:
            toclear = surrounding(pair)[3:]
            for i in toclear:
                board[i[1]][i[0]] = danger(i[0],i[1])
        elif pair[1] == 1:
            toclear = surrounding(pair)[:5]
            for i in toclear:
                board[i[1]][i[0]] = danger(i[0],i[1])
        else:
            for pair in surrounding([x,y]):
                board[pair[1]][pair[0]] = danger([pair[0], pair[1]])
    for i in range(size ** 2):
        x = int(raw_input('Enter col: ')) - 1
        y = int(raw_input('Enter row: ')) - 1
        if [x,y] in mines:
            board[y][x] = 'X'
            printer(board)
            print "Game Over."
            break
        else:
            board[y][x] = danger([x,y])
            if danger([x,y]) == '0':
                clear([x,y])  
            printer(board)




