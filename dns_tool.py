import socket
import requests
import streamlit as st

# ---- Functions ----

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except:
        return None


def reverse_lookup(ip):
    try:
        host = socket.gethostbyaddr(ip)
        return host[0]
    except:
        return "Not available"


def ip_info(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        data = requests.get(url).json()

        return {
            "Country": data.get("country"),
            "City": data.get("city"),
            "ISP": data.get("isp"),
            "Organization": data.get("org")
        }

    except:
        return None


# ---- Streamlit UI ----

st.set_page_config(page_title="DNS Lookup Tool", page_icon="🌐")

st.title("🌐 DNS Lookup & IP Information Tool")

st.write("Enter a domain name to get networking details")

domain = st.text_input("Enter domain (example: google.com)")

if st.button("Check"):

    if domain:

        ip = dns_lookup(domain)

        if ip:
            st.success("DNS Lookup Successful")

            st.subheader("IP Address")
            st.write(ip)

            hostname = reverse_lookup(ip)

            st.subheader("Hostname")
            st.write(hostname)

            info = ip_info(ip)

            if info:
                st.subheader("IP Information")

                st.write("Country:", info["Country"])
                st.write("City:", info["City"])
                st.write("ISP:", info["ISP"])
                st.write("Organization:", info["Organization"])

        else:
            st.error("DNS lookup failed")

    else:
        st.warning("Please enter a domain")