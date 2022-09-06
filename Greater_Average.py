t=int(input())
for i in range(t):
    a,b,c = input().split()
    x = int(a)
    y = int(b)
    z = int(c)
    avg = (x + y) / 2
    if avg > z:
        print("YES")
    else:
        print("NO")
