def cube(n):
    res = 1
    
    for _ in range(3):
        res *= n
    return res
  
n = 5
print(cube(n))
