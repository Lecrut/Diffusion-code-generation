def parse_pairs(input_string):
    pairs = input_string.strip().split()
    parsed_pairs = [(int(pairs[i]), int(pairs[i+1])) for i in range(0, len(pairs), 2)]
    return parsed_pairs

def calculate_averages(data):
    if not data:
        return []
    
    first_elements = [item[0] for item in data]
    second_elements = [item[1] for item in data]
    
    avg_first = sum(first_elements) / len(first_elements)
    avg_second = sum(second_elements) / len(second_elements)
    
    return [avg_first, avg_second]

if __name__ == '__main__':
    sample_input = "1 2 3 4 5 6 7 8"
    parsed_data = parse_pairs(sample_input)
    averages = calculate_averages(parsed_data)
    print(f"{averages=}")