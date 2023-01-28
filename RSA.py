#RSA 임호/복호

from Crypto.Util.number import getPrime
from gmpy2 import next_prime


def euc(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    a0, b0 = a, b
    
    while (b != 0):
        i = a // b
        x0, x1 = x1, x0 - i*x1
        y0, y1 = y1, y0 - i*y1
        
        a = x0*a0 + y0*b0
        b = x1*a0 + y1*b0
    
    return x0
    
def mrs(a, n, z):
    r = 1
    x = a % z
    while (n > 0):
        if (n % 2 == 1):
            r = r * x % z
        x = (x * x) % z
        n = int(n/2)
    
    return r

def enc(m):
    c = mrs(m, e, N)
    
    return c

def dec(c):
    m = mrs(c, d, N)

    return m

#key Gen
p = getPrime(30)
q = next_prime(p)
N = p * q
phiN = (p-1) * (q-1)
e = 65537
d = euc(e, phiN)

while (d < 0):
    d = d + phiN

m = 15
c = enc(m)
p = dec(c)

print(m, c, p)