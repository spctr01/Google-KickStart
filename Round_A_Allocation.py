t = int(input())

for x in range(t):
    n, b =  map(int, input().strip().split(' '))
    l = list(map(int, input().strip().split(' ')))
    
    l.sort()
    count = 0
    sm = 0
    
    
    
    for a in range(len(l)):
        if l[a]>b:
            break
        sm += l[a]
        if sm > b:
            break
        count += 1
        
    print('Case #{}: {}'.format(x+1, count))