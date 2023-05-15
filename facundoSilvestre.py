import numpy as np

def n_dimension():
    try:
        n_input = input('Please insert the size of the squared: ')
        n = int(n_input)
        return n
    except Exception as e:
        print(e)

def input_bombs(inp:str):
    values_plane = input(inp)
    if values_plane == "":
        return []
    values_list = values_plane.split(',')
    values_list_int = [int(i) for i in values_list]
    return values_list_int



if __name__ == '__main__':
    # N, number of the shape of our minesweeper
    n = n_dimension()

    # I'll use Numpy to create the matrix of the minesweeper to better performance
    matrix = np.zeros(shape=(n,n))


    # Position of the bombs for the rows f and the columns c 
    str_rows = f"""Insert bomb's position in rows:
    Maximun values "{n*n}": """
    f = input_bombs(str_rows)
    str_columns = f"""Insert bomb's position in columns:
    Must be "{len(f)}" the number of values: 
    """
    c = input_bombs(str_columns)

    # Fill the matrix with the positions of the bombs
    for p in range(0,len(f)):
        matrix[f[p]][c[p]] = 1

    # Nested list dimension 2, shape N.
    board = [[0 for _ in range(n)] for _ in range(n)]

    # I use list because the result must use strings and with numpy is not posible
    for i in range(n):
        for j in range(n):
            if matrix[i][j] !=1:
                count = 0
                if i > 0:
                    count += matrix[i-1][j]
                if i < n-1:
                    count += matrix[i+1][j]
                if j > 0:
                    count += matrix[i][j-1]
                if j < n-1:
                    count += matrix[i][j+1]
                if i > 0 and j > 0:
                    count += matrix[i-1][j-1]
                if i > 0 and j < n-1:
                    count += matrix[i-1][j+1]
                if i < n-1 and j > 0:
                    count += matrix[i+1][j-1]
                if i < n-1 and j < n-1:
                    count += matrix[i+1][j+1]
            else:
                count = "B"
            board[i][j] = count

    print(board)