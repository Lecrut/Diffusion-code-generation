from typing import Iterator, Sequence, Any

_FIRST_TRUE_SENTINEL = object()

def yield_first_true(sequence: Sequence[bool]) -> Iterator[bool]:
    for element in sequence:
        if element:
            yield True
            return
    yield False

def check_any_true(sequence: Sequence[bool]) -> bool:
    return next(yield_first_true(sequence), False)

if __name__ == '__main__':
    test_data = [False, False, True, False]
    generator = yield_first_true(test_data)
    result = next(generator)
    print(f"Result: {result}")

    empty_data = [False, False, False]
    empty_result = check_any_true(empty_data)
    print(f"Empty Result: {empty_result}")

    true_first_data = [True, False, False]
    true_first_result = check_any_true(true_first_data)
    print(f"True First Result: {true_first_result}")