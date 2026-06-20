class BooleanUtils:
    @staticmethod
    def find_opposite_truth(value):
        return not value

if __name__ == '__main__':
    print(BooleanUtils.find_opposite_truth(True))
    print(BooleanUtils.find_opposite_truth(False))