class MaxPairFinder:
    def __init__(self):
        self._max_pairs = []
    
    def add_pair(self, pair):
        self._max_pairs.append(max(pair))
    
    def get_max_pairs(self):
        return self._max_pairs

if __name__ == '__main__':
    finder = MaxPairFinder()
    sample_pairs = [(10, 5), (20, 3), (15, 2)]
    for pair in sample_pairs:
        finder.add_pair(pair)
        print(f"Added pair {pair}, Current Max Pairs: {finder.get_max_pairs()}")