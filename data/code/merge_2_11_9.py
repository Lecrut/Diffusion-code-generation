import sys
def is_uniform_segment(segment):
    return len(set(segment)) <= 1
class ArrayProcessor:
    def __init__(self, data_list):
        self.data = list(data_list) if isinstance(data_list, (list, tuple)) else []
    def process_segments(self, segment_size=None):
        results = []
        n = len(self.data)
        if not self.data or segment_size is None:
            return [True] * 1
        step = max(1, min(segment_size, n // (segment_size + 1))) if segment_size else 1
        for i in range(n):
            end_idx = min(i + step, n)
            seg = self.data[i:end_idx]
            results.append(is_uniform_segment(seg))
        return results
def main():
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    processor = ArrayProcessor(sample_data)
    flags = processor.process_segments(segment_size=3)
    print(flags)
if __name__ == '__main__':
    main()