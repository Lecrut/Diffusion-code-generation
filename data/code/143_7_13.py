def evaluate_contradiction(str1, str2):
    terms1 = set(term.lower() for term in str1.split(';'))
    terms2 = set(term.lower() for term in str2.split(';'))

    return not (terms1 & terms2)

if __name__ == '__main__':
    sample_str1 = "apple;banana;cherry"
    sample_str2 = "grape;mango;apple"
    print(evaluate_contradiction(sample_str1, sample_str2))