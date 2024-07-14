import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Define the devices for each brand
devices = {
    "Vaporesso": ['ECO NANO', 'GEN AIR', 'GTX', 'XROS', 'XROS MINI', 'XROS 2', 'XROS 2 MINI', 'XROS 3', 'XROS 3 MINI',
                  'XROS 4', 'XROS 4 MINI', 'XROS CUBE', 'XROS 4 PRO'],
    "Voopoo": ['ARGUS P1', 'DORIC', 'DRAG S', 'DRAG X', 'PNP MTL TANK', 'PNP POD TANK', 'TPP POD TANK', 'TPP-X TANK'],
    "Uwell": ['CALIBURN A2', 'CALIBURN A2S', 'CALIBURN A3', 'CALIBURN A3S', 'CALIBURN G', 'CALIBURN G2', 'CALIBURN G3',
              'CALIBURN G3 LITE', 'CALIBURN X'],
    "Geekvape": ['AEGIS U', 'BOOST 2', 'BOOST PRO', 'CERBERUS TANK', 'SONDER Q'],
    "SMOK": ['IPX80', 'NORD 2', 'NORD 4', 'NORD 5', 'NOVO', 'NOVO 2', 'NOVO 2X', 'RPM 5',
             'TFV9 TANK'],
    "Freemax": ['MARVOS', 'MESH PRO 2 TANK', 'MESH PRO TANK'],
    "Aspire": ['GUROO TANK', 'NAUTILUS 2 TANK', 'NAUTILUS 3 TANK', 'NAUTILUS MINI TANK']
}

# Define the compatible pods/coils for each device
compatible_pods_coils = {
    # VAPORESSO
    "ECO NANO": [("VAPORESSO ECO NANO POD (0.8, 1.0)", "images/econano.png")],
    "GEN AIR": [("VAPORESSO GTX COIL (0.4, 0.6, 0.8)", "images/gtx.png")],
    "GTX": [("VAPORESSO GTX COIL (0.4, 0.6, 0.8)", "images/gtx.png")],
    "XROS": [("VAPORESSO XROS Replacement Pod (0.4, 0.6 (2mL/3mL), 0.8 (2mL/3mL), 1.0, 1.2)", "images/xros.png")],
    "XROS MINI": [("VAPORESSO XROS Replacement Pod (0.4, 0.6 (2mL/3mL), 0.8 (2mL/3mL), 1.0, 1.2)", "images/xros.png")],
    "XROS 2": [("VAPORESSO XROS Replacement Pod (0.4, 0.6 (2mL/3mL), 0.8 (2mL/3mL), 1.0, 1.2)", "images/xros.png")],
    "XROS 2 MINI": [("VAPORESSO XROS Replacement Pod (0.4, 0.6 (2mL/3mL), 0.8 (2mL/3mL), 1.0, 1.2)", "images/xros.png")],
    "XROS 3": [("VAPORESSO XROS Replacement Pod (0.4, 0.6 (2mL/3mL), 0.8 (2mL/3mL), 1.0, 1.2)", "images/xros.png")],
    "XROS 3 MINI": [("VAPORESSO XROS Replacement Pod (0.4, 0.6 (2mL/3mL), 0.8 (2mL/3mL), 1.0, 1.2)", "images/xros.png")],
    "XROS 4": [("VAPORESSO XROS Replacement Pod (0.4, 0.6 (2mL/3mL), 0.8 (2mL/3mL), 1.0, 1.2)", "images/xros.png")],
    "XROS 4 MINI": [("VAPORESSO XROS Replacement Pod (0.4, 0.6 (2mL/3mL), 0.8 (2mL/3mL), 1.0, 1.2)", "images/xros.png")],
    "XROS 4 PRO": [("VAPORESSO XROS Replacement Pod (0.4, 0.6 (2mL/3mL), 0.8 (2mL/3mL), 1.0, 1.2)", "images/xros.png")],
    "XROS CUBE": [("VAPORESSO XROS Replacement Pod (0.4, 0.6 (2mL/3mL), 0.8 (2mL/3mL), 1.0, 1.2)", "images/xros.png")],
    # VOOPOO
    "ARGUS P1": [("VOOPOO Argus Replacement Pod (0.7, 1.2)", "images/argus.png")],
    "DRAG S": [("VOOPOO PNP Replacement Coil (1.0, 0.8, 0.6, 0.3, 0.2, 0.15)", "images/pnp.png")],
    "DRAG X": [("VOOPOO PNP Replacement Coil (1.0, 0.8, 0.6, 0.3, 0.2, 0.15)", "images/pnp.png")],
    "PNP MTL TANK": [("VOOPOO PNP Replacement Coil (1.0, 0.8, 0.6, 0.3, 0.2, 0.15)", "images/pnp.png")],
    "PNP POD TANK": [("VOOPOO PNP Replacement Coil (1.0, 0.8, 0.6, 0.3, 0.2, 0.15)", "images/pnp.png")],
    "TPP POD TANK": [("VOOPOO TPP Replacement Coil (0.3, 0.2, 0.15)", "images/tpp.png")],
    "TPP-X TANK": [("VOOPOO TPP Replacement Coil (1.0, 0.8, 0.6, 0.3, 0.2, 0.15)", "images/tpp.png")],
    # UWELL
    "CALIBURN A2": [("UWELL Caliburn A2/A2S Replacement Pod (0.9, 1.2)", "images/caliburna2.png")],
    "CALIBURN A2S": [("UWELL Caliburn A2/A2S Replacement Pod (0.9, 1.2)", "images/caliburna2.png")],
    "CALIBURN A3": [("UWELL Caliburn A3/A3S Replacement Pod (0.8, 1.0)", "images/caliburna3.png")],
    "CALIBURN A3S": [("UWELL Caliburn A3/A3S Replacement Pod (0.8, 1.0)", "images/caliburna3.png")],
    "CALIBURN G": [("UWELL Caliburn G Replacement Pod (0.8, 1.0)", "images/caliburng.png")],
    "CALIBURN G2": [("UWELL Caliburn G2 Replacement Pod (0.8, 1.2)", "images/caliburng2.png")],
    "CALIBURN G3": [("UWELL Caliburn G3 Replacement Pod (0.6, 0.9)", "images/caliburng3.png")],
    "CALIBURN G3 LITE": [("UWELL Caliburn G3 Replacement Pod (0.6, 0.9)", "images/caliburng3.png")],
    "CALIBURN X": [("UWELL Caliburn X Replacement Pod (0.8, 1.0, 1.2)", "images/caliburnx.png")],
    # GEEKVAPE
    "AEGIS U": [("GEEKVAPE Aegis U Replacement Pod (0.7, 1.2)", "images/aegisu.png")],
    "BOOST 2": [("GEEKVAPE Boost/Hero Replacement Coil (0.2, 0.4, 0.6)", "images/boost.png")],
    "BOOST PRO": [("GEEKVAPE Boost/Hero Replacement Coil (0.2, 0.4, 0.6)", "images/boost.png")],
    "CERBERUS TANK": [("GEEKVAPE Cerberus Replacement Coil (0.2, 0.4)", "images/cerberus.png")],
    "SONDER Q": [("GEEKVAPE Sonder Q Replacement Pod (0.6, 0.8, 1.2)", "images/sonderq.png")],
    # SMOK
    "IPX80": [("SMOK RPM/RPM2 Replacement Coil", "images/rpm.png")],
    "NORD 2": [("SMOK Nord/RPM Replacement Coil", "images/rpm.png")],
    "NORD 4": [("SMOK RPM/RPM2 Replacement Coil", "images/rpm.png")],
    "NORD 5": [("SMOK RPM3 Replacement Coil (0.15, 0.23)", "images/rpm3.png")],
    "NOVO": [("SMOK NOVO 2 Replacement Pod (1.0, 1.4)", "images/novo2.png")],
    "NOVO 2": [("SMOK NOVO 2 Replacement Pod (1.0, 1.4)", "images/novo2.png")],
    "NOVO 2X": [("SMOK NOVO 2X Replacement Pod (0.8, 0.9)", "images/novo2x.png")],
    "RPM 5": [("SMOK RPM3 Replacement Coil (0.15, 0.23)", "images/rpm3.png")],
    "TFV9 TANK": [("SMOK TFV9 Replacement Coil (0.15)", "images/tfv9.png")],
    # FREEMAX
    "MARVOS": [("FREEMAX Marvos Replacement Coil (0.15, 0.25, 0.35, 0.5)", "images/marvos.png")],
    "MESH PRO": [("FREEMAX 904L M Replacement Coils (0.15, 0.2)", "images/mpro.png")],
    "MESH PRO 2": [("FREEMAX 904L M Replacement Coils (0.15, 0.2)", "images/mpro.png")],
    # ASPIRE
    "GUROO TANK": [("ASPIRE Guroo Replacement Coil (0.15, 0.3)", "images/guroo.png")],
    "NAUTILUS MINI TANK": [("ASPIRE Nautilus BVC Replacement Coil (0.4, 0.7, 0.7 MESH, 1.8)", "images/nautilus.png")],
    "NAUTILUS 2 TANK": [("ASPIRE Nautilus BVC Replacement Coil (0.4, 0.7, 0.7 MESH, 1.8)", "images/nautilus.png")],
    "NAUTILUS 3 TANK": [("ASPIRE Nautilus BVC Replacement Coil (0.4, 0.7, 0.7 MESH, 1.8)", "images/nautilus.png")],
}

class DeviceSelectorApp(tk.Tk):
    """
    Main application class for the Device Selector app.
    """
    def __init__(self):
        super().__init__()
        self.title("Device Selector")
        self.geometry("400x400")
        self.current_frame = None
        self.current_brand = None  # Keep track of the current brand
        self.show_brand_selection()

    def show_brand_selection(self):
        """
        Display the brand selection screen.
        """
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = BrandSelectionFrame(self, self.show_device_selection)
        self.current_frame.pack(expand=True, fill=tk.BOTH)

    def show_device_selection(self, brand):
        """
        Display the device selection screen for the chosen brand.

        :param brand: The selected brand.
        """
        self.current_brand = brand  # Update the current brand
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = DeviceSelectionFrame(self, brand, self.show_compatible_pods_coils)
        self.current_frame.pack(expand=True, fill=tk.BOTH)

    def show_compatible_pods_coils(self, device):
        """
        Display the compatible pods/coils screen for the chosen device.

        :param device: The selected device.
        """
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = CompatiblePodsCoilsFrame(self, device, self.current_brand, self.show_device_selection)
        self.current_frame.pack(expand=True, fill=tk.BOTH)

class BrandSelectionFrame(tk.Frame):
    """
    Frame for selecting the brand.
    """
    def __init__(self, master, on_brand_select):
        super().__init__(master)
        self.on_brand_select = on_brand_select
        self.create_widgets()

    def create_widgets(self):
        """
        Create and display the widgets for brand selection.
        """
        top_frame = tk.Frame(self)
        top_frame.pack(fill=tk.X, pady=10)

        # Placeholder for alignment with BACK button on the device selection page
        placeholder = tk.Label(top_frame, width=6)
        placeholder.pack(side=tk.LEFT, padx=10)

        label = tk.Label(top_frame, text="What brand of device do you use?", font=("Arial", 18))
        label.pack(side=tk.TOP, pady=10)
        label.place(relx=0.5, rely=0.5, anchor='center')

        # Sort the brand names alphabetically
        sorted_brands = sorted(devices.keys())

        for brand in sorted_brands:
            button = ttk.Button(self, text=brand, command=lambda b=brand: self.on_brand_select(b))
            button.pack(pady=10, ipadx=10, ipady=10)

class DeviceSelectionFrame(tk.Frame):
    """
    Frame for selecting the device.
    """
    def __init__(self, master, brand, on_device_select):
        super().__init__(master)
        self.brand = brand
        self.on_device_select = on_device_select
        self.create_widgets()

    def create_widgets(self):
        """
        Create and display the widgets for device selection.
        """
        top_frame = tk.Frame(self)
        top_frame.pack(fill=tk.X, pady=10)

        back_button = ttk.Button(top_frame, text="← BACK", command=self.master.show_brand_selection)
        back_button.pack(side=tk.LEFT, padx=10)

        label = tk.Label(top_frame, text="What device?", font=("Arial", 18))
        label.pack(side=tk.TOP, pady=10)
        label.place(relx=0.5, rely=0.5, anchor='center')

        button_width = 25  # Set a fixed button width

        for device in sorted(devices[self.brand]):
            button = ttk.Button(self, text=device, width=button_width, command=lambda d=device: self.on_device_select(d))
            button.pack(pady=10, ipadx=10, ipady=10)

class CompatiblePodsCoilsFrame(tk.Frame):
    """
    Frame for displaying compatible pods/coils.
    """
    def __init__(self, master, device, brand, on_back):
        super().__init__(master)
        self.device = device
        self.brand = brand
        self.on_back = on_back
        self.create_widgets()

    def create_widgets(self):
        """
        Create and display the widgets for showing compatible pods/coils.
        """
        top_frame = tk.Frame(self)
        top_frame.pack(fill=tk.X, pady=10)

        back_button = ttk.Button(top_frame, text="← BACK", command=lambda: self.on_back(self.brand))
        back_button.pack(side=tk.LEFT, padx=10)

        label = tk.Label(top_frame, text="Compatible Pods/Coils", font=("Arial", 18))
        label.pack(side=tk.TOP, pady=10)
        label.place(relx=0.5, rely=0.5, anchor='center')

        # Display compatible pods/coils with images and names
        content_frame = tk.Frame(self)
        content_frame.pack(expand=True, fill=tk.BOTH, pady=20)  # Added padding to move images away from the top

        if self.device in compatible_pods_coils:
            for pod_coil_name, image_file in compatible_pods_coils[self.device]:
                container = tk.Frame(content_frame, pady=20)  # Increased padding between images
                container.pack(expand=True, fill=tk.BOTH)

                # Load and display the image
                image_path = os.path.join(os.getcwd(), image_file)  # Ensure the path includes the images directory
                image = Image.open(image_path)
                image = image.resize((200, 200), Image.Resampling.LANCZOS)  # Resize the image to be larger
                photo = ImageTk.PhotoImage(image)

                name_label = tk.Label(container, text=pod_coil_name, font=("Arial", 14))
                name_label.pack(pady=10)

                image_label = tk.Label(container, image=photo)
                image_label.image = photo  # Keep a reference to avoid garbage collection
                image_label.pack(pady=10)

if __name__ == "__main__":
    app = DeviceSelectorApp()
    app.mainloop()




