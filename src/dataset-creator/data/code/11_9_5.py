import sys
def is_uniform_segment(segment):
    if not segment:
        return True
    first_value = segment[0]
    for value in segment:
        if value != first_value:
            return False
    return True
class ArrayProcessor:
    def __init__(self, data_list):
        self.data = list(data_list)
    def analyze_segments(self):
        results = []
        current_segment = [self.data[0]]
        for i in range(1, len(self.data)):
            if self.data[i] != self.data[i - 1]:
                results.append(is_uniform_segment(current_segment))
                current_segment = [self.data[i]]
            else:
                current_segment.append(self.data[i])
        results.append(is_uniform_segment(current_segment))
        return results
if __name__ == '__main__':
    sample_data_1 = [5, 5, 3, 3, 3]
    sample_data_2 = [10, 20, 30, 40]
    processor_1 = ArrayProcessor(sample_data_1)
    flags_1 = processor_1.analyze_segments()
    processor_2 = ArrayProcessor(sample_data_2)
    flags_2 = processor_2.analyze_segments()
    print(f"Sample Data 1 Flags: {flags_1}")
    print(f"Sample Data 2 Flags: {flags_2}")