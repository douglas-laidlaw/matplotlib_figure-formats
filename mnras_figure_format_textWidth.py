import numpy
from matplotlib import rcParams as rc
from matplotlib import pyplot; pyplot.ion()

fig_width_pt = 504.0 						# Get this from LaTeX using \showthe\columnwidth
inches_per_pt = 1.0/72.               		# Convert pt to inch
fig_width = fig_width_pt*inches_per_pt  	# width in inches
fig_height = 0.75 * fig_width
default_fig_size = [6.4, 4.8]
fig_size =  [fig_width,fig_width/3.]
rc['figure.figsize'] = fig_size
scale = 0.5208333333333333
# print(fig_size)

rc['figure.dpi'] = 220.53/2.

rc['text.latex.unicode'] = True
rc['text.latex.preamble'] = [r'\usepackage{newtxmath}'] 

rc['font.family'] = 'serif'
rc['font.serif'] = 'times'
rc['font.cursive'] = 'Zapf Chancery'
rc['font.monospace'] = 'Courier'

rc['ps.useafm'] = True
rc['ps.fonttype'] = 42
rc['pdf.use14corefonts'] = True
rc['text.usetex'] = True #Let TeX do the typsetting

rc['figure.autolayout'] = True

rc['font.size'] = 8
rc['axes.labelsize'] = 8
rc['legend.fontsize'] = 6
rc['xtick.labelsize'] = 8
rc['ytick.labelsize'] = 8
rc['axes.titlesize'] = 8

rc['image.origin'] = 'lower'
rc['image.interpolation'] = 'nearest'
rc['lines.markersize'] = 1 * scale
rc['grid.linewidth'] = rc['grid.linewidth'] * scale * 0.6
rc['lines.linewidth'] = rc['lines.linewidth'] * scale * 0.6
rc['axes.linewidth'] = rc['axes.linewidth'] * scale
rc['xtick.major.width'] = rc['xtick.major.width'] * scale
rc['xtick.minor.width'] = rc['xtick.minor.width'] * scale
rc['ytick.major.width'] = rc['ytick.major.width'] * scale
rc['ytick.minor.width'] = rc['ytick.minor.width'] * scale
rc['backend'] = 'MacOSX'

# \the\textwidth
# \the\columnwidth
# % \the\fontdimen6\font
# \fontname\font\

if __name__=='__main__':
	pyplot.rc('text',usetex=True)
	f, a = pyplot.subplots()
	a.set_xlabel(r'Turbulence (km) \hspace{10pt} \it{y} $y$ $\alpha$')
	a.set_yscale('log')
	a.set_ylim(1e-16, 1e-12)
	a.set_xlim(-0.5, 24.5)
	a.grid(True, which='major', alpha=0.75, linewidth=0.1)
	x = numpy.linspace(0,24,7).astype(int)
	a.set_xticks(x)
	a.set_xticklabels(x)
	# pyplot.savefig('tessst.pdf', dpi=gcf().dpi)
	# pyplot.savefig('tessst.pdf')
