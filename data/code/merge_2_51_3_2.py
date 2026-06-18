import sys
def get_head(safe_list):
    try:
        return safe_list[0]
    except IndexError:
        raise ValueError("Collection is empty") from None
if __name__ == '__main__':
    sample_data = [1, 2, 3]
    head_value = get_head(sample_data)
    print(f"Head value: {head_value}")