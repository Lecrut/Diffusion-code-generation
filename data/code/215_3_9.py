class MaxFinder:
    MAX_SET = {4, 8, 15, 16, 23, 42}
    
    @staticmethod
    def get_max():
        return max(MaxFinder.MAX_SET)

if __name__ == '__main__':
    print(MaxFinder.get_max())