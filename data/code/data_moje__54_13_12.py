class HollowSquare:
    def __init__(self, size):
        self.size = size

    def render(self):
        if self.size <= 0:
            return ''
        if self.size == 1:
            return '*'
        top_bottom = '*' * self.size
        middle = '*' + ' ' * (self.size - 2) + '*'
        return '\n'.join([top_bottom] + [middle] * (self.size - 2) + [top_bottom])

if __name__ == '__main__':
    pattern = HollowSquare(6)
    print(pattern.render())
    print("---")
    print(HollowSquare(3).render())