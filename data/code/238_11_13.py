class HollowSquare:
    @staticmethod
    def create(side_length):
        if side_length < 2:
            return ""
        square = []
        for i in range(side_length):
            if i == 0 or i == side_length - 1:
                square.append('*' * side_length)
            else:
                square.append('*' + ' ' * (side_length - 2) + '*')
        return '\n'.join(square)

if __name__ == '__main__':
    sample_side_length = 4
    print(HollowSquare.create(sample_side_length))