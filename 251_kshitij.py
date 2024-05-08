import numpy as np
import matplotlib.pyplot as plt

# Defining the temp ranges
T_range1 = np.linspace(500, 700, 100) 
T_range2 = np.linspace(300, 400, 100) 
T_range_full = np.linspace(300, 700, 200) 

# Thermal conductivity values for silicon (from empirical data)
k_si = lambda T: 2.4e7 * T**(-1.49) if T >= 500 else 24000  # W/m-K

k1 = 148  # W/m-K (From the paper)
k2 = 84  # W/m-K (From the paper)

k3 = 235  # W/m-K (From the paper)
k4 = 211  # W/m-K (From the paper)

# Plot the thermal conductivity vs. temperature
plt.figure(figsize=(10, 6))

# Plot the empirical data for silicon
plt.plot(T_range_full, [k_si(T) for T in T_range_full], label='Empirical data for silicon')

# Plot the piecewise constant approximations
plt.plot([500, 700], [k1, k1], 'r--', label='Piecewise constant approx. (Fig. 1(b))')
plt.plot([500, 700], [k2, k2], 'r--')
plt.plot([300, 400], [k3, k3], 'g--', label='Piecewise constant approx. (Fig. 1(c))')
plt.plot([300, 400], [k4, k4], 'g--')

plt.xlabel('Absolute Temperature (K)')
plt.ylabel('Thermal Conductivity (W/m-K)')
plt.title('Thermal Conductivity of Silicon')
plt.legend()
plt.grid()
plt.show()