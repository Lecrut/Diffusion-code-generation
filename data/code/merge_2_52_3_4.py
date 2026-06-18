import sys
def yield_until_final(stream):
    for item in stream:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            print(f"Yielded value: {item}")
if __name__ == '__main__':
    sample_data = [10, 20.5, "skip", 30]
    yield_until_final(sample_data)