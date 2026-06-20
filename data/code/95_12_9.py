def read_and_check_integers(a, b, c):
    results = []
    for val in [a, b, c]:
        status = {
            "positivity": val > 0,
            "evenness": val % 2 == 0,
            "magnitude": val < 100
        }
        results.append(status)
    return results

if __name__ == '__main__':
    sample_values = [50, -3, 98]
    print(read_and_check_integers(*sample_values))