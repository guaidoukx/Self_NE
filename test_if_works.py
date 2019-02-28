import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import networkx as nx
# plt.interactive(False)
# G = nx.dodecahedral_graph()
# plt.plot()
# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()
# sphinx_gallery_thumbnail_number = 3
import matplotlib.pyplot as plt
import numpy as np
print(matplotlib.get_backend())
x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.savefig("out/test_result/a.png")