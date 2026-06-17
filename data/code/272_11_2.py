import time
def sort_words(word_list):
    return sorted(word_list)
if __name__ == '__main__':
    sample_list = ["banana", "apple", "cherry", "date", "elderberry"]
    start_time = time.perf_counter()
    sorted_result = sort_words(sample_list)
    end_time = time.perf_counter()
    print(sorted_result)