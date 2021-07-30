import pickle
import matplotlib, matplotlib.pyplot as plt
import numpy as np
import random
import imageio



# data = np.abs(pickle.load(open("data/3_millenium_falcon_truth.pkl", "rb"))['img'])
data = np.abs(pickle.load(open("data/34_totoro_truth.pkl", "rb"))['img'])
# data = np.abs(pickle.load(open("data/1_einstein_truth.pkl", "rb"))['img'])
# data = np.abs(pickle.load(open("data/8_apple_logo_truth.pkl", "rb"))['img'])
# data = (np.sum(imageio.imread("darren.jpeg"), axis=2))# [::4, ::4]
data = data / np.max(data)
# data = np.rot90(data, k=1)
data = np.rot90(data, k=3)

dims = [7, 10]

tiled = np.tile(data, dims)
art = np.empty((data.shape[0] * dims[0], data.shape[1] * dims[1], 4))


all_cmaps = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
all_cmaps.remove('flag')
all_cmaps.remove('flag_r')
all_cmaps.remove('gist_yarg')
all_cmaps.remove('gist_yarg_r')
all_cmaps.remove('gist_gray')
all_cmaps.remove('gist_gray_r')
all_cmaps.remove('binary')
all_cmaps.remove('binary_r')
all_cmaps.remove('Greys')
all_cmaps.remove('Greys_r')
all_cmaps.remove('prism')
random.shuffle(all_cmaps)


cmaps = ['Spectral_r', 'hsv', 'Set3_r', 'twilight_r', 'Blues', 'gist_ncar_r', 'tab20c_r', 'pink_r', 'brg_r', 'GnBu_r', 'winter', 'viridis', 'magma', 'Pastel1_r', 'hot_r']#  []

while len(cmaps) < dims[0] * dims[1]:
    if not all_cmaps[0] in cmaps:
        cmaps.append(all_cmaps[0])
    del all_cmaps[0]

random.shuffle(cmaps)

# cmaps = ['tab20_r', 'PRGn', 'gist_ncar_r', 'ocean', 'jet_r', 'gnuplot_r', 'Spectral_r', 'terrain_r']
# cmaps = ['tab20_r', 'PRGn', 'gist_ncar_r', 'ocean', 'jet_r', 'viridis_r', 'Spectral_r', 'terrain_r']
# cmaps = ['tab20_r', 'PRGn', 'gist_ncar_r', 'ocean', 'jet_r', 'viridis_r', 'Spectral_r', 'gist_stern_r']
# cmaps = ['tab20_r', 'PRGn', 'gist_ncar_r', 'ocean', 'gist_stern', 'viridis_r', 'Spectral_r', 'BrBG_r']

whites = ['gist_stern_r','ocean_r','twilight','terrain_r','tab20c_r','gist_earth_r','magma_r','bone_r']
favorite = ['tab20_r', 'Accent', 'viridis_r', 'PRGn', 'gist_stern', 'gist_ncar_r', 'Spectral_r', 'ocean']
abstract =['Accent','Set2_r','Dark2_r','Paired','Pastel2_r','tab10']

yellows = ['viridis_r','spring_r','cividis_r','gnuplot_r','summer_r','Set3_r','plasma_r','autumn_r']
# grainy = ['tab20c', 'tab20c_r', 'tab20b', 'tab20b_r', 'tab20', 'tab20_r', 'tab10', 'tab10_r','Set1', 'Set1_r', 'Pastel1', 'Pastel1_r', 'Paired', 'Paired_r', 'Dark2', 'Dark2_r', 'Accent', 'Accent_r']
# random.shuffle(grainy)
# cmaps = grainy[:8]


print(cmaps)
print(np.asarray(cmaps).reshape(dims))


cmaps = [matplotlib.cm.get_cmap(x) for x in cmaps]

for x, map in enumerate(cmaps):
    i = (x // dims[1]) * data.shape[0]
    j = (x % dims[1]) * data.shape[1]

    print(x, map.__dict__['name'], i, j)

    art[i:i+data.shape[0], j:j+data.shape[1]] = map(tiled[i:i+data.shape[0], j:j+data.shape[1]])

plt.imsave("out.png", art)

plt.figure(figsize=(13, 13))
plt.imshow(art)
plt.axis('off')
plt.show()