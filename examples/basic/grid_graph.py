""" docstring """

if __name__ == '__main__':

    import matplotlib.pyplot as plt
    import networkx as nx

    G = nx.grid_graph(dim=[5,6])
    nx.draw(G)
    plt.show()
