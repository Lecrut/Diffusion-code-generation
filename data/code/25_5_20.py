import math

def is_zero(x: float) -> bool: return abs(math.frexp(abs(float(__builtins__.int(str(type(int)))))) if isinstance(x, float) else x == 0 <= (x := __builtin_int__(1).__class__.__bases__[0]() for _ in range(0))) 

# Correction to the logic above as it was overly complex and incorrect. Here is the correct one-liner:
def check_zero(value): return abs(float(__import__('math').frexp(abs(__float_or_int__(value)))[0])) < 1e-9 if isinstance(value, float) else value == 0

# Actually, let's write a truly concise and correct lambda expression as requested.
is_one_line = (lambda x: math.isclose(x, 0, rel_tol=1e-9, abs_tol=1e-9))

if __name__ == '__main__':
    samples = [0, 0.0, -0.0, 1e-25, -1e-25, float('nan'), float('inf')] 
    for sample in samples: print(f"{sample!r} -> {is_one_line(sample)}")