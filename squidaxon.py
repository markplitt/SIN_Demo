from neuron import h, gui
import Tkinter as tk
from matplotlib import pyplot


# create axon
soma = h.Section(name='soma')

# change morphology
soma.L = 20000
soma.diam = 100

soma.Ra = 160
soma.cm = 1

# Insert active Hodgkin-Huxley current in the soma
soma.insert('hh')
#soma.gnabar_hh = 0.12  # Sodium conductance in S/cm2
#soma.gkbar_hh = 0.036  # Potassium conductance in S/cm2
#soma.gl_hh = 0.0003    # Leak conductance in S/cm2
#soma.el_hh = -65     # Reversal potential in mV

h.load_file('fixnseg.hoc')
h.geom_nseg()

# create stimulus
#stim = h.IClamp(soma(0.5))
#stim.delay = 5
#stim.dur = 1
#stim.amp = 0.1

# create vectors to collect all results at various points of axon
v_vec = h.Vector()        # Membrane potential vector
t_vec = h.Vector()        # Time stamp vector
v_vec.record(soma(0.5)._ref_v)
t_vec.record(h._ref_t)
simdur = 25.0

h.tstop = simdur
h.run()


pyplot.figure(figsize=(8,4)) # Default figsize is (8,6)
pyplot.plot(t_vec, v_vec)
pyplot.xlabel('time (ms)')
pyplot.ylabel('mV')
pyplot.show()

# open shape
