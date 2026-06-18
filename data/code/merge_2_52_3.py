import sys
def yield_until_final(iterable):
    for item in iterable:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            print(f"Yielding {item}")
            continue
        try:
            val = eval(str(item).replace("'", '"'))
            result = next(val)
            while True:
                yield from result
                if len(result) == 0 or (isinstance(result[0], int) and not isinstance(result[0], bool)):
                    final_val = result[-1]
                    print(f"Final value reached: {final_val}")
                    return
        except Exception as e:
            continue
if __name__ == '__main__':
    data_stream = [
        "range(5)",
        "[1, 2]",
        "{3}",
        "(4,)"
    ]
    result_generator = yield_until_final(data_stream)
    for item in result_generator:
        print(f"Result element: {item}")