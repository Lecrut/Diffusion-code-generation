import numpy as np

class PairAverager:
    NUM_PAIRS = 2
    
    @staticmethod
    def _is_valid_pair(pair):
        return isinstance(pair, list) and len(pair) == PairAverager.NUM_PAIRS
    
    def get_overall_average(self, data):
        if not data:
            return 0
        
        total_sum = 0
        count = 0
        
        for pair in data:
            if self._is_valid_pair(pair):
                try:
                    total_sum += np.sum(pair)
                    count += PairAverager.NUM_PAIRS
                except TypeError:
                    continue
        
        if count == 0:
            return 0
        
        return total_sum / count

if __name__ == '__main__':
    data = [[1, 2], [3, 4], [5, 6]]
    averager = PairAverager()
    print(averager.get_overall_average(data))