def fetch_third_item(source):
    if hasattr(source, '__getitem__'):
        try:
            return source[2]
        except IndexError:
            raise IndexError("Iterable must have at least three items")
    iterator = iter(source)
    try:
        next(iterator)
        next(iterator)
        return next(iterator)
    except StopIteration:
        raise IndexError("Iterable must have at least three items")

def run_demonstration():
    numeric_list = [5, 10, 15, 20, 25]
    string_data = "abcdefgh"
    generator_source = (x * x for x in range(100))
    
    first_result = fetch_third_item(numeric_list)
    print(first_result)
    
    second_result = fetch_third_item(string_data)
    print(second_result)
    
    third_result = fetch_third_item(generator_source)
    print(third_result)

if __name__ == '__main__':
    run_demonstration()