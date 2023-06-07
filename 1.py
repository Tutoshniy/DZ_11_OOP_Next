class Matrix:
    '''Простые действия с матрицами'''

    def __init__(self, rows, cols):
        '''Создание матрицы'''
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for j in range(cols)] for i in range(rows)]

    def __str__(self):
        '''Вывод матрицы'''
        return "\n".join([" ".join([str(self.matrix[i][j]) for j in range(self.cols)]) for i in range(self.rows)])

    def __eq__(self, other):
        '''Сравнение двух матриц'''
        if self.rows != other.rows or self.cols != other.cols:
            return 'Матрицы не равны'
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return 'Матрицы не равны'
        return 'Матрицы равны'

    def __add__(self, other):
        '''Сумма двух матриц'''
        if self.rows != other.rows or self.cols != other.cols:
            raise AttributeError("Матрицы должны быть одинакового размера")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return f'Сумма матриц = \n{result}'


matrix1 = Matrix(2, 2)
matrix1.matrix = [[2, 3], [3, 4]]
matrix2 = Matrix(2, 2)
matrix2.matrix = [[3, 4], [5, 6]]
print(matrix1 == matrix2)
print(matrix1 + matrix2)
