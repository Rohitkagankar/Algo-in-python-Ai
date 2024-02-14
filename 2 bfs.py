Graph={
    '5':['3','7'],
    '3':['2','4'],
    '2':[],
    '4':['8'],
    '7':['8'],
    '8':[]
}

visited=[]
queue=[]

def bfs (visited,Graph,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        m=queue.pop(0)
        print(m, end=" ")
        for neighbour in Graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("following is the Breadth-first search")
bfs(visited,Graph,'5')
        