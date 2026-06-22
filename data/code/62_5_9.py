factor_config = {
    'start': 1,
    'end_condition': 'sqrt',
    'include_complement': True
}

def compute_factors(n):
    limit = int(n**0.5)
    small_factors = (i for i in range(factor_config['start'], limit + 1) if n % i == 0)
    result_set = set()
    for f in small_factors:
        result_set.add(f)
        if factor_config['include_complement'] and f * f != n:
            result_set.add(n // f)
    return sorted(list(result_set))

if __name__ == '__main__':
    target = 120
    factors = compute_factors(target)
    print(factors)