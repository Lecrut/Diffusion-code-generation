def find_middle_element(t):
    if not t:
        raise ValueError("Sequence is empty")
    return t[len(t) // 2]

if __name__ == '__main__':
    sample_tuples = (
        (1, 2, 3),
        (10, 20, 30, 40),
        ('a', 'b', 'c', 'd', 'e'),
        (99,),
        ()
    )
    for t in sample_tuples:
        try:
            result = find_middle_element(t)
            print(f"Middle of {t} is {result}")
        except ValueError as e:
            print(f"Error for {t}: {e}")