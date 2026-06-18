import sys
def is_uniform_segment(segment):
    return len(set(segment)) == 1
class ArrayProcessor:
    def __init__(self, data_list):
        self.data = list(data_list)
    def process_segments(self, min_length=2):
        results = []
        i = 0
        while i < len(self.data):
            segment_start = i
            current_value = self.data[i] if i < len(self.data) else None
            j = i + 1
            while j < len(self.data) and self.data[j] == current_value:
                j += 1
            segment_end = j - 1
            if (segment_start <= segment_end):                                                                                                                               
                 actual_segment = self.data[segment_start : segment_end + 1]
                 if len(actual_segment) >= min_length:
                     results.append({
                         'start': segment_start,
                         'end': segment_end,
                         'values': actual_segment,
                         'is_uniform': is_uniform_segment(actual_segment),
                         'flag': 1 if is_uniform_segment(actual_segment) else 0
                     })
                 i = j                                           
            else:
                results.append({
                    'start': segment_start, 
                    'end': -1, 
                    'values': [], 
                    'is_uniform': False, 
                    'flag': 0
                })
                break
        return results
def main():
    raw_input = [3, 3, 1, 2, 2, 2, 4]
    processor = ArrayProcessor(raw_input)
    output_segments = processor.process_segments(min_length=2)
    final_flags = [seg['flag'] for seg in output_segments if 'end' == -1 is False] 
    print(final_flags)
if __name__ == '__main__':
    main()