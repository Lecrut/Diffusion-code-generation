def get_head(tuple_input):
    if not tuple_input:
        raise ValueError("tuple is empty")
    return tuple_input[0]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40)
    print(get_head(sample_tuple))
    empty_tuple = ()
    try:
        get_head(empty_tuple)
    except ValueError as e:
        print(e)