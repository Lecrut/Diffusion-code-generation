class HollowSquare:
    def __init__(self, side_length):
        self.side_length = side_length

    def create_hollow_square(self):
        if self.side_length < 2:
            return ""
        square = []
        for i in range(self.side_length):
            if i == 0 or i == self.side_length - 1:
                square.append('*' * self.side_length)
            else:
                square.append('*' + ' ' * (self.side_length - 2) + '*')
        return '\n'.join(square)

if __name__ == '__main__':
    square1 = HollowSquare(4)
    print(square1.create_hollow_square())