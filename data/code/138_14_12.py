if __name__ == '__main__':
    truth_table = {
        (True, True): True,
        (True, False): False,
        (False, True): True,
        (False, False): True
    }

    for a in [False, True]:
        for b in [False, True]:
            print(f"{a} -> {b}: {truth_table[(a, b)]}")