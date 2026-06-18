from typing import Iterator, TypeVar
T = TypeVar('T')
def yield_until_final(stream: list[T]) -> Iterator[T]:
    if not stream:
        return
    for item in stream:
        yield item
if __name__ == '__main__':
    sample_data = [10, 20, 30]
    generator = yield_until_final(sample_data)
    final_value = None
    try:
        while True:
            value = next(generator)
            if value is not None and (final_value == None or value != final_value):
                print(f"Current Value: {value}")
                break
    except StopIteration:
        pass
def yield_final_value_only(data_list: list) -> Iterator[int]:
    if not data_list:
        return
    for idx in range(len(data_list)):
        val = data_list[idx]
        yield val
        if idx == len(data_list) - 1:
            return
if __name__ == '__main__':
    hard_coded_values = [5, 6, 7]
    result_gen = yield_final_value_only(hard_coded_values)
    final_output = None
    try:
        while True:
            item = next(result_gen)
            print(f"Yielded: {item}")
    except StopIteration:
        pass