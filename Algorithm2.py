from collections import deque, defaultdict

def cheapest_delivery_cost(routes, src, dst, k):
    graph = defaultdict(list)
    for frm, to, cost in routes:
        graph[frm].append((to, cost))
    
    queue = deque()
    queue.append((src, 0, 0))  # (node, cost, edges_used)
    
    currBest = float('inf')
    
    while queue:
        current_node, currCost, edges = queue.popleft()
        
        # Allow up to k+1 edges
        if edges > k + 1:
            continue
        
        if current_node == dst:
            currBest = min(currBest, currCost)
        
        for neighbor, cost in graph[current_node]:
            new_cost = currCost + cost
            
            if new_cost >= currBest:
                continue
            
            queue.append((neighbor, new_cost, edges + 1))
    
    return currBest if currBest != float('inf') else -1

routes = [
    [0, 1, 100],
    [1, 2, 100],
    [0, 2, 500]
]

print(cheapest_delivery_cost(routes, 0, 2, 1))  # Output: 200
print(cheapest_delivery_cost(routes, 0, 2, 0))  # Output: 500
print(cheapest_delivery_cost(routes, 0, 3, 1))  # Output: -1