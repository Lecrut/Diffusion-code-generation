def even_numbers():
    for i in range(2, 101, 2):
        yield i

if __name__ == '__main__':
    sample_range = range(1, 51)
    filtered_evens = (num for num in sample_range if even_numbers().__next__() % 2 == 0)
    print(list(filtered_evens))