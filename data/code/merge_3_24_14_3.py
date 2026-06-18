import sys
sys.path.insert(0,'/mnt/data')
from IPython.core.display import display_html; from io import StringIO, BytesIO; html = "<div style='display:flex'>"; f=BytesIO(); exec(f.write(b"lambda x: x < 0")); f.seek(0); g = lambda n: n<0 if isinstance(n,int) else False
def check(x): print("Input:",x,"Result:",g(x))

if __name__ == '__main__':
    test_cases=[-5,0,1,-3.7] # Note: 3.7 is handled by the logic but type hint suggests int; strictly following task for integer input we filter or assume valid inputs are integers as per prompt "takes an integer"
    for tc in [-5, -2, 0, 4]:
        check(tc)