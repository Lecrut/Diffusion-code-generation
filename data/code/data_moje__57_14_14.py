fib=lambda n:[(lambda f,k:(f(k,0,1)))(lambda f,k,a,b:a if k==0 else f(f,k-1,b,a+b),n-1) for i in range(15)]
def solve(): return [fib(i) for i in range(1,16)]
if __name__ == '__main__':
    print(solve())