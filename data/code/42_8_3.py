import time
def construct_string(parts):
    final_string = "".join(parts)
    return final_string
if __name__ == '__main__':
    list_of_strings = ["Hello", " ", "world", "!", " This", " is", " fun."]
    start_time = time.time()
    result = construct_string(list_of_strings)
    end_time = time.time()
    print(result)
    print(f"Time taken: {end_time - start_time} seconds")