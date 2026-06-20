def evaluate_logic(p, q):
    r = p ^ q
    return (p and q) or (not p and r)

if __name__ == '__main__':
    results = {
        (True, True): evaluate_logic(True, True),
        (True, False): evaluate_logic(True, False),
        (False, True): evaluate_logic(False, True),
        (False, False): evaluate_logic(False, False)
    }
    print(results)