def sort_and_analyze(string_list):
    sorted_list = sorted(string_list)
    total_length = sum(len(s) for s in sorted_list)
    return total_length
if __name__ == '__main__':
    sample_list = ["banana", "apple", "cherry", "date"]
    result = sort_and_analyze(sample_list)
    print(result)