import requests

# Set up the API request parameters
url = "http://<grafana-server>/api/dashboards/db"
headers = {
    "Authorization": "Bearer <api-token>",
    "Content-Type": "application/json"
}
payload = {
    "dashboard": {
        "id": 1, # replace with your dashboard ID
        "timezone": "browser",
        "panels": [
            {
                "id": 2, # replace with your panel ID
                "type": "graph",
                "title": "CPU and Memory Usage",
                "targets": [
                    {
                        "expr": "node_cpu_seconds_total{mode='idle'}",
                        "refId": "A"
                    },
                    {
                        "expr": "node_memory_MemAvailable_bytes",
                        "refId": "B"
                    }
                ],
                "legend": {
                    "show": True
                },
                "xaxis": {
                    "show": True
                },
                "yaxes": [
                    {
                        "format": "short",
                        "label": "CPU Usage",
                        "show": True
                    },
                    {
                        "format": "bytes",
                        "label": "Memory Usage",
                        "logBase": 1,
                        "show": True
                    }
                ]
            }
        ],
        "refresh": "5s",
        "schemaVersion": 21,
        "version": 1
    }
}

# Send the API request and retrieve the data
response = requests.post(url, headers=headers, json=payload)
data = response.json()
