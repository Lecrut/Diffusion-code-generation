def find_adjacent_mismatches(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    
    length = len(sequence)
    if length < 2:
        return []
    
    mismatches = []
    for idx in range(length - 1):
        current = sequence[idx]
        next_val = sequence[idx + 1]
        if current is not next_val and current != next_val:
            mismatches.append({
                "index": idx,
                "left": current,
                "right": next_val
            })
            
    return mismatches

class MismatchFinder:
    def __init__(self, data):
        self.data = data
    
    def get_results(self):
        return find_adjacent_mismatches(self.data)

if __name__ == '__main__':
    sample_values = [10, 20, 20, 30, 40, 40, 50]
    
    finder_instance = MismatchFinder(sample_values)
    results = finder_instance.get_results()
    
    for record in results:
        print(record)