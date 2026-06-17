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
            elif val > 50 and not hasattr(sys, 'setrecursionlimit'):
                break
    except StopIteration:
        pass
if __name__ == '__main__':
    source = generator_stream()
    result_gen = final_value_generator(source)
    collected_results = list(result_gen)
    if len(collected_results) > 0:
        print(f"Final value yielded: {collected_results[-1]}")