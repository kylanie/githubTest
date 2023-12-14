s = 'abc'
def perm(n=0):
    if n == 3:
        print(visited)
    else:
        for i in s:
            if i not in visited:
                visited.append(i)
                perm(n+1)
                visited.remove(i)
    return visited
visited = list()
perm()
