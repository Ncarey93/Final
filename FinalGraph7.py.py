#Directed Graph - Supply Chain for Semiconductor Industry. 
import networkx as nx #from pip install
import matplotlib.pyplot as plt #from pip install

# Creating a Directed Graph 
def create_graph():
    G = nx.DiGraph() #sets up graph and type
    factories = [f'Factory{i}' for i in range(1, 21)]
    G.add_nodes_from(factories)

#NODES = Factorys 1 - 20
    nodes = [ 'Factory 1', 'Factory 2', 'Factory 3', 'Factory 4', 'Factory 5', 'Factory 6',
        'Factory 7', 'Factory 8', 'Factory 9', 'Factory 10', 'Factory 11', 'Factory 12',
        'Factory 13', 'Factory 14', 'Factory 15', 'Factory 16', 'Factory 17', 'Factory 18',
        'Factory 19', 'Factory 20']
    G.add_nodes_from(nodes)

#EDGES = Routes 1 - 20 (route distance in miles) : (time in mins)

    edges = [ ('Factory 1', 'Factory 2', {'route distance': 5, 'minutes apart' : 7.5} ),
          ('Factory 2', 'Factory 3', {'route distance': 12, 'minutes apart' : 18} ),
          ('Factory 3', 'Factory 4', {'route distance': 21, 'minutes apart' : 31.5} ),
          ('Factory 4', 'Factory 5', {'route distance': 16, 'minutes apart' : 24} ),
          ('Factory 5', 'Factory 6', {'route distance': 30, 'minutes apart' : 45} ),
          ('Factory 6', 'Factory 7', {'route distance': 18, 'minutes apart' : 27} ),
          ('Factory 7', 'Factory 8', {'route distance': 3, 'minutes apart' : 4.5} ),
          ('Factory 8', 'Factory 9', {'route distance': 48, 'minutes apart' : 72}),
          ('Factory 9', 'Factory 10', {'route distance': 83, 'minutes apart' : 124.5}),
          ('Factory 10', 'Factory 11', {'route distance': 46, 'minutes apart' : 69} ),
          ('Factory 11', 'Factory 12', {'route distance': 75, 'minutes apart' : 112.5} ),
          ('Factory 12', 'Factory 13', {'route distance': 71, 'minutes apart' : 106.5} ),
          ('Factory 13', 'Factory 14', {'route distance': 8, 'minutes apart' : 12} ),
          ('Factory 14', 'Factory 15', {'route distance': 14, 'minutes apart' : 21} ),
          ('Factory 15', 'Factory 16', {'route distance': 55, 'minutes apart' : 43.6} ),
          ('Factory 16', 'Factory 17', {'route distance': 103, 'minutes apart' : 154.5} ),
          ('Factory 17', 'Factory 18', {'route distance': 122, 'minutes apart' : 183} ),
          ('Factory 18', 'Factory 19', {'route distance': 230, 'minutes apart' : 345} ),
          ('Factory 19', 'Factory 20', {'route distance': 147, 'minutes apart' : 220} ),
          ('Factory 20', 'Factory 1', {'route distance': 1147, 'minutes apart' : 2868} ) ]
    G.add_edges_from(edges)

        # Print edges to verify weights
    for u, v, data in G.edges(data=True):
        print(f"Data from {u} to {v} with attributes {data}")

    return G
#This Function helps to visualize the graph 
def visualize_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels = True, node_size = 3000, node_color = 'lightgreen',
            font_size = 12, font_weight = 'bold')
    edge_labels = nx.get_edge_attributes(G, 'route distance')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show

    #ALGORITHM SECTION: 
    #Dijstra's Algorithm (Shortest Path Algorithm) this will make use of the 'minutes apart' data.
def shortest_path(G, source, target, weight = 'minutes apart'):
    return nx.shortest_path(G, source = source, target = target, weight = weight)

    #Algorithm for (Kruskal's) Minimum Spanning Tree (MST)
    #Sorting all the edges in the graph by their weight (e.g., route distance or minutes apart).
#Adding edges to the MST in increasing order of weight, ensuring no cycles are formed, until all vertices are connected.
def minimum_spanning_tree(G, weight = 'route distance'):
    UG = G.to_undirected()
    mst = nx.minimum_spanning_tree(UG, weight+weight)
    return list(mst.edges(data = True))

#Function for DFS - depth-first-search (not making use of weight)
def depth_first_search(G, source):
    return list(nx.dfs_edges(G, source = source))

# Main Function to RUN project

def main():
    G = create_graph()
    visualize_graph(G)

    print("Shortest Path (by minutes apart):", shortest_path(G, 'Factory 1', 'Factory 20', weight = 'minutes apart'))
    print("Minimum Spanning Tree (by route distance):", minimum_spanning_tree(G))
    print("DFS:", depth_first_search(G, 'Factory 1'))

if __name__ == "__main__":
    main()