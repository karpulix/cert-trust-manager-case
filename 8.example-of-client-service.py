from elasticsearch import Elasticsearch

ca_cert_path = "/ca-trust-bundle.pem"

es = Elasticsearch(
    ["https://elasticsearch-es-http.elasticsearch.svc:9200"],
    ca_certs=ca_cert_path,
    verify_certs=True,
)

try:
    response = es.info()
    print("Cluster info:", response)
except Exception as e:
    print(f"Error connecting to Elasticsearch: {e}")
    