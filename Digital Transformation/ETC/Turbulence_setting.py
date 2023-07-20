import tkinter as tk
from tkinter import messagebox


def calculate_reynolds_number():
    try:
        density = float(density_entry.get())
        velocity = float(velocity_entry.get())
        dynamic_viscosity = float(dynamic_viscosity_entry.get())

        # Characteristic length scale (e.g., hydraulic diameter for internal flows)
        # Replace this value with the appropriate length scale for your flow scenario
        length_scale = float(length_scale_entry.get())

        reynolds_number = (density * velocity * length_scale) / dynamic_viscosity

        reynolds_number_label.config(text=f"Reynolds Number: {reynolds_number:.2f}")

        # Enable the Calculate Turbulent Intensity button
        calculate_ti_button.config(state=tk.NORMAL)
    except ValueError:
        messagebox.showerror("Input Error",
                             "Please enter valid numeric values for Density, Velocity, Dynamic Viscosity, "
                             "and Characteristic Length Scale.")


def calculate_turbulent_intensity():
    try:
        reynolds_number = float(reynolds_number_label.cget("text").split()[-1])

        # Empirical correlation for estimating turbulent intensity based on Reynolds number
        # Please note that this correlation is a simplified example and might not be accurate for all cases.
        # For real-world applications, use relevant correlations based on flow conditions and geometry.
        turbulent_intensity = 0.16 * reynolds_number ** (-(1 / 8)) * 100

        turbulent_intensity_label.config(text=f"Turbulent Intensity: {turbulent_intensity:.2f}%")
    except ValueError:
        messagebox.showerror("Calculation Error", "Reynolds Number not found. Please calculate it first.")


# Create the main application window
app = tk.Tk()
app.title("Turbulent Intensity Calculator")

# Create labels and entry fields for input parameters
density_label = tk.Label(app, text="Density (kg/m³):")
density_label.grid(row=0, column=0)
density_entry = tk.Entry(app)
density_entry.grid(row=0, column=1)

velocity_label = tk.Label(app, text="Velocity (m/s):")
velocity_label.grid(row=1, column=0)
velocity_entry = tk.Entry(app)
velocity_entry.grid(row=1, column=1)

dynamic_viscosity_label = tk.Label(app, text="Dynamic Viscosity (Pa·s):")
dynamic_viscosity_label.grid(row=2, column=0)
dynamic_viscosity_entry = tk.Entry(app)
dynamic_viscosity_entry.grid(row=2, column=1)

length_scale_label = tk.Label(app, text="Hydraulic diameter (m):")
length_scale_label.grid(row=3, column=0)
length_scale_entry = tk.Entry(app)
length_scale_entry.grid(row=3, column=1)

# Create a button to calculate Reynolds number
calculate_re_button = tk.Button(app, text="Calculate Reynolds Number", command=calculate_reynolds_number)
calculate_re_button.grid(row=4, columnspan=2)

# Create a label to display the Reynolds number result
reynolds_number_label = tk.Label(app, text="")
reynolds_number_label.grid(row=5, columnspan=2)

# Create a button to calculate turbulent intensity (disabled initially)
calculate_ti_button = tk.Button(app, text="Calculate Turbulent Intensity", command=calculate_turbulent_intensity,
                                state=tk.DISABLED)
calculate_ti_button.grid(row=6, columnspan=2)

# Create a label to display the turbulent intensity result
turbulent_intensity_label = tk.Label(app, text="")
turbulent_intensity_label.grid(row=7, columnspan=2)

# Start the main event loop
app.mainloop()
