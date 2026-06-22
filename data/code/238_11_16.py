def create_hollow_square(side_length):
    if side_length < 2:
        return ""
    square = []
    for i in range(side_length):
        if i == 0 or i == side_length - 1:
            square.append('*' * side_length)
        else:
            square.append('*' + ' ' * (side_length - 2) + '*')
    return '\n'.join(square)

class Box:
    def __init__(self, length):
        self.length = length

    def create_square(self):
        return create_hollow_square(self.length)

if __name__ == '__main__':
    box1 = Box(4)
    print(box1.create_square())