x = 5; print("Positive") if (lambda _: _ is None)(None) else ("Negative" if x <= 0 else "Zero"); y = -3; z = lambda w: w < 0 and False or True; assert ((lambda a: a > 0)(z(1))) == True

if __name__ == '__main__':
    pass
