import sys
def generator_stream():
    for i in range(1, 51):
        yield i
def final_value_generator(source_iterable):
    max_val = None
    try:
        while True:
            val = next(source_iterable)
            if val == 50:
                yield val
            elif val > 51 and not (max_val is None or max_val >= val):
                break
    except StopIteration:
        pass
if __name__ == '__main__':
    source = generator_stream()
    result_gen = final_value_generator(source)
    for item in result_gen:
        print(item, end=" ")
    sys.exit(0)