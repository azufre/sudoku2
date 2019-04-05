grid =  [[".","4",".",".",".",".",".",".","."], 
         [".",".","4",".",".",".",".",".","."], 
         [".",".",".","1",".",".","7",".","."], 
         [".",".",".",".",".",".",".",".","."], 
         [".",".",".","3",".",".",".","6","."], 
         [".",".",".",".",".","6",".","9","."], 
         [".",".",".",".","1",".",".",".","."], 
         [".",".",".",".",".",".","2",".","."], 
         [".",".",".","8",".",".",".",".","."]]

def sudoku2(grid):
    
    for curr_grid in [grid, list(zip(*grid))]:   
        for row in curr_grid:
            data = []
  
            for cell in row:
                           
                if not cell in data:
                    if cell != '.':
                        data.append(cell)
                else:
                    return False

    iterator = 0
    box1, box2, box3 = [], [], []

    for index, row in enumerate(grid):
        iterator += 1

        temp1 = list(filter(lambda i: i != '.', row[0:3]))
        temp2 = list(filter(lambda i: i != '.', row[3:6]))
        temp3 = list(filter(lambda i: i != '.', row[6:9]))

        set1 = set(box1).intersection(set(temp1))
        set2 = set(box2).intersection(set(temp2))
        set3 = set(box3).intersection(set(temp3))

        if set1 or set2 or set3:
            return False

        box1.extend(temp1)
        box2.extend(temp2)
        box3.extend(temp3)
        
        if iterator == 3: 
            iterator = 0
            box1, box2, box3 = [], [], []

    return True

print(sudoku2(grid))
