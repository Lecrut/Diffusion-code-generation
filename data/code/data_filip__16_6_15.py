import sys

def run_length_encode(strings):
    if not strings:
        return []
    
    result = []
    current_str = strings[0]
    count = 1
    
    for i in range(1, len(strings)):
        if strings[i] == current_str:
            count += 1
        else:
            result.append((current_str, count))
            current_str = strings[i]
            count = 1
    
    result.append((current_str, count))
    
    return result

if __name__ == '__main__':
    sample_data = ["A", "A", "B", "B", "B", "C"]
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)