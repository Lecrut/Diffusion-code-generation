import sys
def get_list_head(data: list) -> any:
    if not data:
        raise ValueError("List is empty")
    return data[0]
if __name__ == '__main__':
    sample_data = [1, 2, 3]
    try:
        head = get_list_head(sample_data)
        print(f"Head of list: {head}")
        empty_sample = []
        try:
            _ = get_list_head(empty_sample)
        except ValueError as e:
            print(f"Error handling test - {e}")
    except Exception:
        sys.exit(1)