import heapq
def sort_strings_generator(data):
    return sorted(data)
if __name__ == '__main__':
    large_dataset = ["banana", "apple", "cherry", "date", "elderberry"] * 10000 + [f"item_{i}" for i in range(500)]
    input_data = (f"{chr(97 + i % 26)}{i}" for i in range(len(large_dataset))) 
    sorted_result = list(sort_strings_generator(input_data))
    print(sorted_result[:5])